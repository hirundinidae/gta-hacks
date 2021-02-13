export const siteTitle = 'Our App'

export default function Header({ children }) {
  return (
    <header>
      <div className="wrapper">
        <h1>{ siteTitle }</h1>
      </div>
    </header>
  )
}