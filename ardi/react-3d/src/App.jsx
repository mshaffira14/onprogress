/* eslint-disable no-unused-vars */
import { BrowserRouter as Router,Route,Routes } from "react-router-dom";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Home from "./pages/Home";
import Project from "./pages/Project";

function App() {

  return (
    <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/project" element={<Project />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
    </Router>
  );
}

export default App
