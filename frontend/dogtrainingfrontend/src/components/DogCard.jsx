import React from 'react'
import { Avatar } from "@material-tailwind/react";

const DogCard = (props) => {
  return (
    <div className='bg-blue-100 w-full h-[30%] flex justify-start items-center gap-24 pl-24 rounded-xl mb-2'>
        <Avatar
          src={props.photo}
          alt="photo of a dog"
          size="xxl"
          className='w-[180px] h-[180px] p-1'
          withBorder={true}
        />
        <div className='flex flex-col'>
          <h1 className='text-6xl'>{props.name}</h1>
          <p className='text-3xl'>{props.age} years old</p>
        </div>
    </div>
  )
}

export default DogCard