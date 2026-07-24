import { useEffect } from "react";
import api from "../api/axios";

function Dashboard() {

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

    

    return (

        <div>

            <h1>
                ALPA Dashboard
            </h1>

        </div>

    );

}

export default Dashboard;