import Header from './header'

// add types of layouts (home, article, profile, etc.)
// in Layout arguments and use if statements to identify

export default function Layout({ children }) {
  return (
    <div className="layout">
      <Header />
      <main>
        { children }
      </main>
    </div>
  )
}