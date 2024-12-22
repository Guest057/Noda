import React, { useState } from 'react';

const AskForm = () => {
    const [question, setQuestion] = useState('');
    const [loading, setLoading] = useState(false);
    const [response, setResponse] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const res = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question }),
            });

            if (!res.ok) throw new Error('Failed to submit');

            const data = await res.json();
            setResponse(data);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="ask-form">
            <button onClick={() => setLoading(false)}>
                ⏸️
            </button>

            <form onSubmit={handleSubmit}>
                <input
                    id="massaqe-input"
                    type="text"
                    name="question"
                    placeholder="Message for Ollama"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    required
                    disabled={loading}
                />

                <button type="submit" disabled={loading}>
                    ▶️
                </button>

                {loading && <span id="prompt-loader">Loading...</span>}
            </form>

            {response && (
                <div id="response">
                    {JSON.stringify(response)}
                </div>
            )}
        </div>
    );
};

export default AskForm;
