import react from "react"

import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Predict from './pages/Predict'
import Login from "./pages/Login"
import Register from "./pages/Register"
import Navbar  from "./pages/Navbar"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

import './App.css';

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
    <Navbar />
      <Routes>
      <Route path="/" element={<Home/>} />
        <Route
          path="/predict"
          element={
            <ProtectedRoute>
              <Predict />
            </ProtectedRoute>
          }
        />
         
        
        
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App