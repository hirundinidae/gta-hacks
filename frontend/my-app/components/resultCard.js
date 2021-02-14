export default function ResultCard({ name, questions, answers, tags }) {
  return (
    <div className="result-card w-2/5 h-auto mx-6 mb-8 p-8 rounded-xl shadow-lg">
      <h1>{ name }</h1>
      <p>{ questions }</p>
      <p>{ answers }</p>
      <div className="flex flex-row">
        {
          tags && tags.map(tag => {
            return <span
                    key={tag.id}
                    className="py-1 px-4 mt-4 mr-2 border-4 border-blue-600 text-blue-600 font-bold rounded-full"
                  >{ tag.name }</span>
          })
        }
      </div>
    </div>
  )
}