db.createUser({
    user: "miio",
    pwd: "miio2020",
    roles: [
        {
            role: "readWrite",
            db: "challengedb"
        },
    ],
})