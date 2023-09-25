import React,{useState} from 'react'
import { Link } from 'react-router-dom'
import Navbar from '../../components/Navbar'
import {HiSpeakerWave} from 'react-icons/hi2';
import RecordVoiceSkin3 from '../../components/RecordVoiceSkin3';

const Quess3 = () => {
  const [color,setColor]=useState('bg-color');

  const changeColor=()=>{
  setColor('gray-600');
  }
  

  return (
    <div>
    <Navbar url="/skinques2" loginUser="true" title="Skin Health" />

    <div className="w-[100vw]  flex flex-col  bg-bgall h-[calc(100vh-100px)]">

    <div className='flex text-center'>
        
        {/* questions */}
        <div className='w-1/5 text-center pt-10  border-r-4 border-gray-300 h-[calc(100vh-100px)]'>
            <div className='bg-[#D1E8FF] py-3 text-gray-600'>Question 1</div>
            <div className='bg-[#D1E8FF]  py-3 text-gray-600'>Question 2</div>
            <div className='bg-[#D1E8FF]   py-3 text-gray-600'>Question 3</div>
            <div className=' py-3 text-gray-600'>Question 4
            </div>
        </div>

        {/* recording */}
        <div className='flex flex-col h-[calc(100vh-100px)] items-center mt-[70px] text-center ml-[370px]'>
       
        <div className='flex justify-center items-center flex-col' >
          <span className=" flex justify-center items-center font-[600] text-black text-[18px]">
          Question 3
          <span className={`text-bgcolor font-bold text-[30px] mx-4 cursor-pointer text-${color}`} onClick={changeColor}><HiSpeakerWave/></span>
          </span>
          <span className=" font-[600] mt-[20px] text-gray-400 text-[18px]">
          Please press the button to record your answer
          </span>
        </div>
        
        <div>
            <RecordVoiceSkin3/>
        </div>

        {/* button */}
        <Link to="/skinques4">
        <button className="mt-[40px] fixed botton-[80px] right-[80px] bg-bluebtn py-3 px-12 text-white rounded-lg ">
          Proceed
        </button>
      </Link>

        <div>

        </div>
        </div>

    </div>

    </div>
    </div>
  )
}

export default Quess3