/* eslint-disable no-unused-vars */
import { Loader } from '@react-three/drei'
import { Canvas } from '@react-three/fiber'
import React,{Suspense} from 'react'
import DeathStar from '../components/DeathStars'

const Home = () => {
  const adJustStarforScreenSize =  () =>{
    let screenScale,Screenposition;
    screenScale = [0.6,0.6,0.6]
    Screenposition = [0,-6.5,-43.4]

    return [screenScale,Screenposition]
  }

  const [StarScale,Starposition] = adJustStarforScreenSize()
    return (
    <section className='w-full h-screen relative bg-black overflow-hidden'>
      <Canvas
      className='w-full h-screen bg-transparent'
      camera={{ near: 0.1, far:1000}}
      >

        <Suspense fallback={<Loader/>}>
            <DeathStar
            position={Starposition}
            scale = {StarScale}
            rotation={[0,0,0,]}/>
        </Suspense>

      </Canvas>
    </section>
  )
}

export default Home
