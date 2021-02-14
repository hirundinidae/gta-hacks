export default function TeamCard({ name, title, colour }) {
  return (
    <figure className="team-card">
      <div className={`circle ` + colour}></div>
      <div className="details">
        <h1>{ name }</h1>
        <p>{ title }</p>
      </div>
    </figure>
  )
}