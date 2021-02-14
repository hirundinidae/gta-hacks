import { useState } from 'react'
import Layout from '../components/layout'
import ResultCard from '../components/resultCard'
import { useFormik } from 'formik'
import axios from 'axios'

export default function Search() {
  const [results, setResults] = useState(null)

  const formik = useFormik({
    initialValues: {
      text: '',
    },
    onSubmit: async (values) => {
      const url = `http://localhost:8000/api/resources/?search=${values.text}`

      // fetch(url, {
      //   method: 'GET',
      //   body: null,
      //   headers: {'Content-Type': 'application/json'},
      // })
      //   .then(res => res.json())
      //   .then(data => data.forEach(element => results.push(element))) // display the data
      //   .catch(error => alert(error))

      const response = await axios.get(url)
      setResults(response.data)
    },
  })

  return (
    <Layout>
      <section className="pt-24">
        <div className="wrapper">
          <div className="content">
            <h1>Search</h1>
            <p>Type the resource you're looking for.</p>
            <form onSubmit={formik.handleSubmit}>
              <input
                id="text"
                name="text"
                type="text"
                placeholder="Resource name..."
                onChange={formik.handleChange}
                value={formik.values.text}
              />
      
              <button type="submit">Submit</button>
            </form>
          </div>
        </div>
      </section>
      <section>
        <div className="wrapper">
          <div className="content">
            {
              results &&
              results.map(result => {
                return (
                  <ResultCard 
                    key={ result.id }
                    name={ result.name }
                  />
                )
              })
            }
          </div>
        </div>
      </section>
    </Layout>
  )
}