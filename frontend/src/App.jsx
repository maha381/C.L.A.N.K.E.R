import { useState } from 'react'
import './App.css'


function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')

  	async function send() {
		if (!input.trim()) return

		const userMsg = { role: 'user', text: input }

		setMessages([...messages, userMsg])
		setInput('')

		try {
			const res = await fetch('http://localhost:8000/chat', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ message: userMsg.text }),
			})
			if (!res.ok) throw new Error(`HTTP ${res.status}`)
			const data = await res.json()          // or await res.text()
			setMessages((m) => [...m, { role: 'assistant', text: data.reply }])
			} catch (err) {
			console.error(err)
			setMessages((m) => [...m, { role: 'assistant', text: 'Error: ' + err.message }])
			}
		}
  
  return (
	<center>
		<div>
		<h1>Jarvis - Test Chat</h1>
		<div id="messages">
			{messages.map((m, i) => (
			<p key={i}>
				<b>{m.role}:</b> {m.text}
			</p>
			))}
		</div>
		<input
			type="text"
			value={input}
			onChange={(e) => setInput(e.target.value)}
			onKeyDown={(e) => e.key === 'Enter' && send()}
			placeholder="Type a message..."
			className='chat-input'
		/>
		<button className='send-button' onClick={send}>Send</button>
		</div>
	</center>
  )
}

export default App
