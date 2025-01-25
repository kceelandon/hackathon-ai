// add the card variables still name, img, rating, hours, links

function YelpCard() {
    return (
        <div className="grid grid-cols-2 rounded-md w-full shadow-md border border-gray-300">
            <div className="grid p-4">
                <h1 className="text-center text-2xl font-bold">Din Tai Fung</h1>
                <div>
                    <h2 className="font-bold">Rating</h2>
                    <p>5/5</p>
                </div>
                <div>
                    <h2 className="font-bold">Hours</h2>
                    <p>7am-10pm</p>
                </div>
                <div>
                    <h2 className="font-bold">Links</h2>
                    <a href="">Yelp Page</a>
                </div>
            </div>

            <div className="overflow-hidden">
                <img
                    src="https://s3-media0.fl.yelpcdn.com/bphoto/9vqdaloZxzPcDX5Cxlx2Sg/348s.jpg"
                    alt="Din Tai Fung"
                    className="w-full h-full object-cover"
                />
            </div>
        </div>

    )
}

export default YelpCard