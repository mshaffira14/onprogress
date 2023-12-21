import {useState} from 'react'

export const SkillCreate = () => {
  const [formvalues,setformvalues]= useState({
    name: "",
    slug: ""
  })

  const onChange = (e) => {
    const {name,value} = e.target;
    setformvalues({...formvalues,[name]: value})
  }
  
  return (
    <div className="mt-12">
      <form
        action=""
        className="max-w-md mx-auto p-4 bg-white shadow-md rounded-sm"
      >
        <div className="space-y-6">
          <div className="mb-4">
            <label htmlFor="name" className="block mb-2 text-sm font-medium">
              Name
            </label>
            <input name="name"
              value={formvalues["name"]}
              onChange={onChange}
              className="border border-gray-300 text-gray-900 text-sm rounded-md block w-full p-2"
            />
          </div>

          <div className="mb-4">
            <label htmlFor="Slug" className="block mb-2 text-sm font-medium">
              Slug
            </label>
            <input
              name="slug"
              value={formvalues["slug"]}
              onChange={onChange}
              className="border border-gray-300 text-gray-900 text-sm rounded-md block w-full p-2"
            />
          </div>

          <div className="my-4">
            <button className="px-4 py-2 bg-indigo-500 hover:bg-indigo-700 text-white rounded-md">
              Store
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}
