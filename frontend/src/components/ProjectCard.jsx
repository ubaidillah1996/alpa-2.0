import { useState } from "react";

import api from "../api/axios";

import ProjectInsight from "./ProjectInsight";

import ProductivityScore from "./ProductivityScore";


function ProjectCard({ project }) {


    const [insight, setInsight] = useState(null);

    const [score, setScore] = useState(null);

    const [loadingInsight, setLoadingInsight] = useState(false);

    const [loadingScore, setLoadingScore] = useState(false);

    const fetchInsight = async () => {

        try {

            setLoadingInsight(true);


            // await new Promise(
            //     resolve => setTimeout(resolve, 1000)
            // ); testing loading...


            const response =
                await api.get(
                    `/projects/${project.id}/insight`
                );


            setInsight(response.data);


        } catch(error) {

            console.log(error);


        } finally {

            setLoadingInsight(false);

        }

    };

    const fetchScore = async () => {

        try {

            setLoadingScore(true);


            const response =
                await api.get(
                    `/projects/${project.id}/score`
                );


            setScore(response.data);


        } catch(error) {

            console.log(error);


        } finally {

            setLoadingScore(false);

        }

    };



    return (

        <div
            style={{
                border: "1px solid #ccc",
                padding: "15px",
                marginBottom: "10px",
                borderRadius: "8px"
            }}
        >

            <h3>
                {project.title}
            </h3>


            <p>
                {project.description}
            </p>


            <button
                onClick={fetchInsight}
                disabled={loadingInsight}
            >
                {
                    loadingInsight
                    ? "Loading..."
                    : "View AI Insight"
                }
            </button>



            {
                insight && (

                    <ProjectInsight
                        insight={insight}
                    />

                )
            }

            {
                score && (

                    <ProductivityScore
                        score={score}
                    />

                )
            }

            <button
                onClick={fetchScore}
                disabled={loadingScore}
            >
                {
                    loadingScore
                    ? "Loading..."
                    : "View Productivity Score"
                }
            </button>


        </div>

    );

}


export default ProjectCard;