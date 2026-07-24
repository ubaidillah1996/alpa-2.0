import ProjectCard from "./ProjectCard";


function ProjectList({ projects }) {

    return (

        <div>

            <h2>
                Projects
            </h2>


            {
                projects.map((project) => (

                    <ProjectCard
                        key={project.id}
                        project={project}
                    />

                ))
            }


        </div>

    );

}


export default ProjectList;