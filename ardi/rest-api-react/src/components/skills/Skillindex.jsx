/* eslint-disable array-callback-return */
/* eslint-disable react-hooks/exhaustive-deps */
/* eslint-disable no-unused-vars */
import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export const Skillindex = () => {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
   const getSkills = async () => {
     try {
 const apiSkills = await axios.get("http://localhost:8000/api/v1/skills");

       setSkills(apiSkills.data.data);
     } catch (error) {
       console.error("Error fetching skills:", error.message);
     }
   };


    getSkills();
  }, []);

  return (
    <div className="mt-12">
      <div className="flex justify-end m-2 p-2">
        <Link to="/skills/create" className="px-4 py-2 bg-indigo-500 hover:bg-indigo-700 text-white rounded-md">
          New Skill 
        </Link>
      </div>
      <div className="relative overflow-x-auto">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                id
              </th>
              <th scope="col" className="px-6 py-3">
                Name
              </th>
              <th scope="col" className="px-6 py-3">
                Slug
              </th>
              <th scope="col" className="px-6 py-3">
                Category
              </th>
            </tr>
          </thead>
          <tbody>
            {skills.map((skill) => {
              return (
                <tr
                  key={skill.id} // Add a key for each item in the array
                  className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                  >
                  <td className="py-4 px-6">{skill.id}</td>
                  <td className="py-4 px-6">{skill.name}</td>
                  <td className="py-4 px-6">{skill.slug}</td>
                  <td className="py-4 px-6">Edit/delete</td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
