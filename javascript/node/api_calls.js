const axios = require("axios");

/* ASYNC AWAIT VERSION */
async function apiCall() {
	const photos = await axios.get(
		"https://jsonplaceholder.typicode.com/photos"
	);
	photos.map((photo) => {
		console.log(photo);
	});
}

apiCall();

/* CALLBACK VERSION */
axios.get("https://jsonplaceholder.typicode.com/photos").then((results) => {
	todos = results.data;
	todos.map((todo) => {
		console.log(todo.url);
	});
});

/* Promise.all VERSION */
async function run() {
	const [data1, data2, data3] = await Promise.all([
		axios.get("https://jsonplaceholder.typicode.com/photos"),
		axios.get("https://jsonplaceholder.typicode.com/comments"),
		axios.get("https://jsonplaceholder.typicode.com/todos"),
	]);
	console.log(data1, data2, data3);
}

run();
