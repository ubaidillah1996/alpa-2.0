function UserProfile({ user }) {

    return (

        <div>

            <h2>
                Hello, {user.full_name} 👋
            </h2>


            <p>
                Email: {user.email}
            </p>


            <p>
                Role: {user.role}
            </p>


        </div>

    );

}


export default UserProfile;