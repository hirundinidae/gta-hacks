export default function ResultCard({ name, questions, answers, tags }) {
  return (
    <div className="result-card w-2/5 h-auto mx-6 mb-8 p-6 rounded-xl shadow-lg border-2">
      <h1>{ name }</h1>
      <div className="flex flex-row mt-6">
        <a href={questions} target="_blank" className="p-2 bg-gray-100 font-bold w-28 rounded-lg hover:text-blue-600 border-2 border-gray-100 hover:border-2 hover:border-blue-600 transition-all mr-4">
          Question
        </a>
        {
          answers && 
          <a href={answers} target="_blank" className="p-2 bg-gray-100 font-bold w-28 rounded-lg hover:text-blue-600 border-2 border-gray-100 hover:border-2 hover:border-blue-600 transition-all mr-4">
            Answer
          </a>
        }
      </div>
      <div className="flex flex-row m-2">
        {
          tags && tags.slice(0, 3).map(tag => {
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