export const siteTitle = 'Resourca'

// if logged in --> show profile button, else --> show log in button

export default function Header() {
  return (
    <header>
      <div className="wrapper">
        <h1>
          { siteTitle }
        </h1>
        <button>
          Profile
        </button>
      </div>
    </header>
  )
}