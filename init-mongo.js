//conn = new Mongo();
//db = conn.getDB("challengedb");

db.createUser({
    user: "miio",
    pwd: "miio2020",
    roles: [
        {
            role: "readWrite",
            db: "challengedb",
        },
        {
            role: "userAdminAnyDatabase",
            db: "admin",
        }
    ],
})