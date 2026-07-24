function ProjectInsight({ insight }) {

    return (

        <div>

            <h2>
                AI Insight 🤖
            </h2>


            <h3>
                Insights
            </h3>


            {
                insight.insights.map((item, index) => (

                    <p key={index}>
                        {item}
                    </p>

                ))
            }



            <h3>
                Recommendations
            </h3>


            {
                insight.recommendations.map((item, index) => (

                    <p key={index}>
                        {item}
                    </p>

                ))
            }


        </div>

    );

}


export default ProjectInsight;