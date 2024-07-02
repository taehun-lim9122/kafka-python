import asyncio
import json
import websockets
import time

async def binance_websocket_data(symbol):
    uri = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@ticker"

    last_message_time = 0
    min_time_between_requests = 1.0  # 연속 요청 사이의 최소 시간 (초)

    async with websockets.connect(uri) as websocket:
        print(f"{uri}에 연결되었습니다.")

        while True:
            try:
                current_time = time.time()

                # 요청 속도 제어
                if current_time - last_message_time < min_time_between_requests:
                    await asyncio.sleep(min_time_between_requests - (current_time - last_message_time))

                last_message_time = time.time()

                message = await websocket.recv()
                print(json.loads(message))

            except websockets.ConnectionClosed:
                print("연결이 예기치 않게 닫혔습니다.")
                break
            except Exception as e:
                print(f"오류 발생: {e}")
                continue

# 예제 사용
if __name__ == "__main__":
    symbol = "btcusdt"  # 원하는 심볼로 변경하세요
    asyncio.run(binance_websocket_data(symbol))
