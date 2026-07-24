import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";


import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


function App() {

  return (

    <BrowserRouter>

      <Routes>

    <Route 
        path="/"
        element={
            <h1>ALPA Dashboard</h1>
        }
    />


    <Route
        path="/login"
        element={<Login />}
    />

    <Route
        path="/dashboard"
        element={<Dashboard />}
    />

      </Routes>

    </BrowserRouter>

  )
}


export default App;
