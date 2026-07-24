import { useEffect } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";

function Dashboard() {
    
    const navigate = useNavigate();

    useEffect(() => {

        fetchProjects();

    }, []);

    const fetchProjects = async () => {

        try {

            const response =
                await api.get("/projects");

            console.log(response.data);

        } catch(error) {

            console.log(error);

        }

    };

    const logout = () => {

        localStorage.removeItem(
            "token"
        );


        navigate("/login");

    };



    return (

        <div>

            <h1>
                ALPA Dashboard
            </h1>


            <button
                onClick={logout}
            >
                Logout
            </button>


        </div>

    )

}

export default Dashboard;