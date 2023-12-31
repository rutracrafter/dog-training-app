import React from 'react'
import { Button } from "@material-tailwind/react";

const Home = () => {
  return (
    <div className='w-screen h-screen flex justify-center items-center'>
        <div className='bg-blue-gray-200 w-[60%] h-full'>
            <Button>Button</Button>
        </div>
    </div>
  )
}

export default Home