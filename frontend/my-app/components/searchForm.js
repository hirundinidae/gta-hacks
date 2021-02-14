import { useFormik } from 'formik'

export default function SearchForm() {
  const formik = useFormik({
    initialValues: {
      text: '',
    },

    onSubmit: values => {
      const url = `http://localhost:8000/api/resources/?search=${values.text}`

      fetch(url, {
        method: 'GET',
        body: null,
        headers: { 'Content-Type': 'application/json' },
      })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(error => alert(error))
    },
  })

  return (
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
  )
}