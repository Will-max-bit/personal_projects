import React, { useState } from "react";
import './App.css';
// importing components
import Form from "./components/form";
import Todolist from "./components/todolist"

function App() {
  const [inputText, setInputText] = useState("");
  return (
    <div className="App">
      <header>
      <h1> Wills Todo list </h1>
      </header>
      <Form setInputText={setInputText}/>
      <Todolist />
    </div>
  );
}

export default App;
