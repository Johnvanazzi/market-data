print("-------------- Start Mongo setup ----------------");
db.createUser(
    {
        user: "user",
        pwd: "pwd",
        roles: ["readWrite"]
    }
);

print("-------------- End Mongo setup ----------------");
