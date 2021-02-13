import { useFormik } from 'formik'

export default function IndexSearchForm() {
  const formik = useFormik({
    initialValues: {
      text: '',
    },

    onSubmit: values => {
      alert(JSON.stringify(values, null, 2))
    },
  })

  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="text">Resource</label>
        <input
          id="text"
          name="text"
          type="text"
          onChange={formik.handleChange}
          value={formik.values.text}
        />
 
      <button type="submit">Submit</button>
    </form>
  )
}