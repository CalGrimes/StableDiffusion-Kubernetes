import logo from './logo.svg';
import DarkNavPage from './components/dark_nav_with_overlap';
// Filename - App.js

import React from "react";
import {
	BrowserRouter as Router,
	Routes,
	Route,
} from "react-router-dom";
import Home from "./pages/Home.jsx";
import Demo from "./pages/Demo.jsx";
// import About from "./pages/about";
// import Blogs from "./pages/blogs";
// import SignUp from "./pages/signup";
// import Contact from "./pages/contact";

function App() {
	return (
		<Router>
			<Routes>
				<Route exact path="/" element={<Home />} />
				<Route path="/demo" element={<Demo />} />
				{/* <Route
					path="/contact"
					element={<Contact />}
				/>
				<Route path="/blogs" element={<Blogs />} />
				<Route
					path="/sign-up"
					element={<SignUp />}
				/> */}
			</Routes>
		</Router>
	);
}

export default App;
