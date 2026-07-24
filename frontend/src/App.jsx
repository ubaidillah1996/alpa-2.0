import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./components/ProtectedRoute";

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
        element={
        <ProtectedRoute>
            <Dashboard />
        </ProtectedRoute>
        }
    />

      </Routes>

    </BrowserRouter>

  )
}


export default App;
