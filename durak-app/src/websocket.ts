const socketUrl = `ws://localhost:8000/ws`;

export const connectToWebSocket = (roomId: number, playerId: number) => {
    const socket = new WebSocket(`${socketUrl}/${roomId}/${playerId}`);

    socket.onopen = () => {
        console.log("Connected to WebSocket");
    };

    socket.onmessage = (event) => {
        const message = JSON.parse(event.data);
        // Handle incoming WebSocket messages here
    };

    socket.onclose = () => {
        console.log("WebSocket connection closed");
    };

    socket.onerror = (error) => {
        console.error("WebSocket error:", error);
    };

    return socket;
};
