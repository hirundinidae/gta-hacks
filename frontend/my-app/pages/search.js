import SearchForm from '../components/searchForm'
import Layout from '../components/layout'
import { useFormik } from 'formik'

export default function Search() {
  const formik = useFormik({
    initialValues: {
      text: '',
    },
    onSubmit: values => {
      const url = `http://localhost:8000/api/resources/?search=${values.text}`

      fetch(url, {
        method: 'GET',
        body: null,
        headers: {'Content-Type': 'application/json'},
      })
        .then(res => res.json())
        .then(data => console.log(data)) // display the data
        .catch(error => alert(error))
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
    </Layout>
  )
}