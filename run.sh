#!/usr/bin/env bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_DIR="$BASE_DIR/.pids"

if [ "$1" == "stop" ]; then
    fuser -k 8000/tcp 8001/tcp 8002/tcp 8003/tcp 8004/tcp >/dev/null 2>&1
    rm -f "$PID_DIR"/*.pid
    exit 0
fi

mkdir -p "$PID_DIR"
SERVICES=("tts:src/app.py" "llm:src/api.py" "stt:src/app.py" "avatar:src/server.py" "memory:src/app.py")

for service in "${SERVICES[@]}"; do
    IFS=":" read -r name script <<< "$service"
    cd "$BASE_DIR/services/$name" || continue
    python "$script" > "$PID_DIR/$name.log" 2>&1 &
    echo $! > "$PID_DIR/$name.pid"
done

echo "Use tail -f .pids/*.log to see logs."