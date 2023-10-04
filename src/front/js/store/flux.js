const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			auth: false,
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			registro: async (email, name, password) => {
				try {
					const response = await fetch(process.env.BACKEND_URL + "/api/user", {
						method: "POST",
						body: JSON.stringify({
							name: name,
							email: email,
							password: password,
						}),
						headers: {
							"Content-type": "application/json"
						}
					})
				} catch (error) {
					console.log(error)
				}
			},

			login: async (email, password) => {
				console.log(email, password)
				try {
					const response = await fetch(process.env.BACKEND_URL + "/api/login", {
						method: "POST",
						body: JSON.stringify({
							email: email,
							password: password,
						}),
						headers: {
							"Content-type": "application/json"
						}
					})
					const data = await response.json()
					localStorage.setItem("token", data.access_token)
					setStore({
						auth: true
					})
				} catch (error) {
					console.log(error)
				}
			},
			logout: () => {
				localStorage.removeItem("token")
				setStore({
					auth: false
				})
			},

			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			}
		}
	};
};

export default getState;
