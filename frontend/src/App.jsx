import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Button from '@mui/material/Button';
import YelpCard from './components/YelpCard';

function App() {
  const [city, setCity] = useState("seattle");
  const [radius, setRadius] = useState("");
  const [cuisine, setCuisine] = useState("");
  const [numRestaurants, setNumRestaurants] = useState(1);

  const handleSubmit = () => {
    console.log({
      city,
      radius,
      cuisine,
      numRestaurants,
    });
  };

  return (
    <div className="grid grid-cols-3 justify-center">
      <div className='col-span-1 p-4'>
        <h1 className="text-5xl font-bold">Food Crawler</h1>
        <div className="grid grid-rows-4 gap-4 mt-4">
          <div>
            <label htmlFor="city" className="block text-lg font-medium">
              City
            </label>
            <select
              id="city"
              name="city"
              value={city}
              onChange={(e) => setCity(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="seattle">Seattle</option>
              <option value="new-york">New York</option>
              <option value="los-angeles">Los Angeles</option>
              <option value="dallas">Dallas</option>
              <option value="las-vegas">Las Vegas</option>
            </select>
          </div>
          <div>
            <label htmlFor="radius" className="block text-lg font-medium">
              Radius
            </label>
            <input
              type="number"
              id="radius"
              name="radius"
              value={radius}
              onChange={(e) => setRadius(e.target.value)}
              placeholder="Enter Radius"
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          <div>
            <label htmlFor="cuisine" className="block text-lg font-medium">
              Cuisine
            </label>
            <input
              type="text"
              id="cuisine"
              name="cuisine"
              value={cuisine}
              onChange={(e) => setCuisine(e.target.value)}
              placeholder="Enter cuisine"
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          <div>
            <label htmlFor="numRestaurants" className="block text-lg font-medium">
              Number of Restaurants
            </label>
            <input
              type="number"
              id="numRestaurants"
              name="numRestaurants"
              value={numRestaurants}
              onChange={(e) => setNumRestaurants(Number(e.target.value))}
              min="1"
              max="5"
              className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            />
          </div>
          <div className="flex justify-center mt-4">
            <button
              type="button"
              onClick={handleSubmit}
              className="px-4 py-2 bg-blue-600 text-white font-semibold rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Submit
            </button>

          </div>
        </div>
      </div>
      <div className='col-span-2 grid p-4'>
          {/* <h1 className='text-3xl bold'>Search to find a food crawl for you!</h1> */}
          <YelpCard />
      </div>
    </div>
  );
}

export default App
