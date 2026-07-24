import { useEffect, useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";
import ProjectList from "../components/ProjectList";
import DashboardLayout from "../components/DashboardLayout";
import UserProfile from "../components/UserProfile";
import ActivitySummary from "../components/ActivitySummary";
function Dashboard() {
    
    const navigate = useNavigate();

    const [projects, setProjects] = useState([]);

    const [user, setUser] = useState(null);

    const [activitySummary, setActivitySummary] = useState(null);

    useEffect(() => {

        fetchProjects();

        fetchProfile();

        fetchActivitySummary();

    }, []);

    const fetchProjects = async () => {

        try {

            const response =
                await api.get("/projects");

            setProjects(response.data);

        } catch(error) {

            console.log(error);

        }

    };

    const fetchProfile = async () => {

        try {

            const response =
                await api.get("/users/me");


            setUser(response.data);


        } catch(error) {

            console.log(error);

        }

    };

    const fetchActivitySummary = async () => {

        try {

            const response =
                await api.get("/activities/summary");


            setActivitySummary(response.data);


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

        <DashboardLayout>


            <h1>
                ALPA Dashboard
            </h1>

            {
                user && (
                    <UserProfile
                        user={user}
                    />
                )
            }

            {
                activitySummary && (

                    <ActivitySummary
                        summary={activitySummary}
                    />

                )
            }


            <button
                onClick={logout}
            >
                Logout
            </button>


            <ProjectList
                projects={projects}
            />


        </DashboardLayout>

    )

}

export default Dashboard;