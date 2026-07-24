import { useState } from "react";

import api from "../api/axios";
import { useNavigate } from "react-router-dom";

function Login(){

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");


    const handleLogin = async () => {

        try {

            const formData = new FormData();

            formData.append(
                "username",
                email
            );

            formData.append(
                "password",
                password
            );


            const response = await api.post(
                "/auth/login",
                formData
            );


            localStorage.setItem(
                "token",
                response.data.access_token
            );

            console.log("Login successful");


        } catch(error){

            console.log(error);

        }

    }

    const handleTest = async () => {

    try {

        const response =
            await api.get("/projects");

        console.log(response.data);

    } catch(error){

        console.log(error);

    }

    }


    return (

        <div>

            <h1>
                ALPA Login
            </h1>


            <input
                placeholder="Email"
                value={email}
                onChange={
                    e => setEmail(e.target.value)
                }
            />


            <input
                placeholder="Password"
                type="password"
                value={password}
                onChange={
                    e => setPassword(e.target.value)
                }
            />


            <button
                onClick={handleLogin}
            >
                Login
            </button>

        </div>

    )

}


export default Login;
