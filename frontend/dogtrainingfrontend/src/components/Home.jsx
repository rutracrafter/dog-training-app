import React, { useState, useEffect } from 'react'
import DogCard from "./DogCard";
import axios from 'axios'

const Home = () => {
  const [dogsData, setDogsData] = useState([]);

  useEffect(() => {
    const Url = 'http://127.0.0.1:8000/dogs/';
    axios.get(Url)
    .then((response) => {
      setDogsData(response.data)
      console.log(dogsData)
    })
    .catch(() => {
      console.log("Error fetching data from {Url}")
    })
  }, []);

  return (
    <div className='w-screen h-screen flex justify-center items-center'>
        <div className='bg-blue-gray-200 w-[60%] h-[70%] rounded-xl flex justify-center items-center'>
            <div className='bg-red-200 w-[70%] h-[80%] rounded-xl overflow-y-auto'>
                {dogsData.map((dog, index) => <DogCard key={index} photo={dog.photo} name={dog.name} age={dog.age} />)}
            </div>
        </div>
    </div>
  )
}

export default Home