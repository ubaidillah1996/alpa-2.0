function ProductivityScore({ score }) {

    return (

        <div>

            <h2>
                Productivity Score 📊
            </h2>


            <p>
                Score:
                {score.productivity_score}
                /100
            </p>


            <p>
                Level:
                {score.level}
            </p>


        </div>

    );

}


export default ProductivityScore;