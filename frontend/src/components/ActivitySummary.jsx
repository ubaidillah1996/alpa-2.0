function ActivitySummary({ summary }) {

    return (

        <div>

            <h2>
                Activity Summary 📈
            </h2>


            <p>
                Total Activities:
                {summary.total_activities}
            </p>


            <p>
                Coding:
                {summary.coding}
            </p>


            <p>
                Learning:
                {summary.learning}
            </p>


            <p>
                Planning:
                {summary.planning}
            </p>


            <p>
                Review:
                {summary.review}
            </p>


            <p>
                Most Active Type:
                {summary.most_active_type}
            </p>


        </div>

    );

}


export default ActivitySummary;