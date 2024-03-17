export function Tool() {
    const [prompt, setPrompt] = React.useState('');
    const [image, setImage] = React.useState('');

    const redis = new Redis(6379);

    function handleClick(e) {
        e.preventDefault();

        // Monitor Redis for changes
        redis.monitor((err, monitor) => {
            monitor.on('monitor', (time, args, rawReply) => {
                console.log(time + ": " + args); // Logs all commands processed by Redis server
            });
        });

        // Send data to the backend via POST
        fetch('http://localhost:8000/', {
            method: 'POST', 
            mode: 'cors', 
            body: JSON.stringify(prompt) // body data type must match "Content-Type" header
        }).then(response => response.json())
        .then(data => {
            setImage(data.image);
            document.getElementById('image').innerHTML = `<img src="${data.image}" alt="Generated Image" className="rounded-md" />`;
        });
    }

    return (
        <div className="justify-center text-center pb-12 px-4 sm:px-6 lg:px-8 bg-white md:max-w-3xl md:mx-auto rounded-md border-black border-2 space-y-6">
            <div className="font-semibold tracking-tight mt-4">
                <h1 className="text-2xl text-gray-800">AI Image Generator</h1>
                <p className="text-sm text-gray-600">Powered by Stable Diffusion</p>
            </div>
            <div id="image" className="flex justify-center h-96">
                <img src="https://via.placeholder.com/300" alt="Generated Image" className="rounded-md" />
            </div>
            <form id="form" className="flex justify-center space-x-2" onSubmit={handleClick}>
                <input type="text" className="w-1/2 border-black border-2 rounded-md px-2" placeholder="Enter a Prompt" value={prompt} onChange={e => setPrompt(e.target.value)} />
                <button type="submit" className="bg-black text-white rounded-md px-4 py-2">Generate</button>
            </form>
        </div>
    );
}