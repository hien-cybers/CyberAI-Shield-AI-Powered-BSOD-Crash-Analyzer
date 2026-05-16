import React, { useState } from 'react';

const styles = {
  container: { maxWidth: '600px', margin: '50px auto', padding: '30px', fontFamily: 'Arial, sans-serif', backgroundColor: '#1e1e2e', color: '#cdd6f4', borderRadius: '12px', boxShadow: '0 4px 20px rgba(0,0,0,0.3)' },
  title: { textAlign: 'center', color: '#89b4fa', marginBottom: '25px' },
  formGroup: { marginBottom: '15px', display: 'flex', flexDirection: 'column' },
  label: { marginBottom: '5px', fontSize: '14px', color: '#a6adc8' },
  input: { padding: '10px', borderRadius: '6px', border: '1px solid #45475a', backgroundColor: '#313244', color: '#fff', fontSize: '16px' },
  button: { width: '100%', padding: '12px', backgroundColor: '#89b4fa', border: 'none', borderRadius: '6px', color: '#11111b', fontSize: '16px', fontWeight: 'bold', cursor: 'pointer', marginTop: '10px', transition: '0.2s' },
  resultBox: { marginTop: '25px', padding: '15px', backgroundColor: '#252538', borderRadius: '8px', borderLeft: '5px solid #a6e3a1' },
  resultTitle: { margin: '0 0 10px 0', color: '#a6e3a1' },
  error: { color: '#f38ba8', marginTop: '10px', textAlign: 'center' }
};

function App() {
  const [formData, setFormData] = useState({ Bugcheck_String: '', Faulting_Module: '', Crash_Code: '' });
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setPrediction('');

    try {
      // Ép gọi thẳng đến IP số của Backend Python
      const response = await fetch('http://127.0.0.1:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Có lỗi xảy ra khi kết nối server.');

      const data = await response.json();
      setPrediction(data.root_cause_prediction);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🛡️ CyberAI Shield Dashboard</h2>
      <form onSubmit={handleSubmit}>
        <div style={styles.formGroup}>
          <label style={styles.label}>Bugcheck String (Mã lỗi lỗi hệ thống):</label>
          <input style={styles.input} type="text" name="Bugcheck_String" value={formData.Bugcheck_String} onChange={handleChange} placeholder="Ví dụ: 0x1A" required />
        </div>
        <div style={styles.formGroup}>
          <label style={styles.label}>Faulting Module (File gây lỗi):</label>
          <input style={styles.input} type="text" name="Faulting_Module" value={formData.Faulting_Module} onChange={handleChange} placeholder="Ví dụ: nt!MmAccessFault" required />
        </div>
        <div style={styles.formGroup}>
          <label style={styles.label}>Crash Code (Tên lỗi):</label>
          <input style={styles.input} type="text" name="Crash_Code" value={formData.Crash_Code} onChange={handleChange} placeholder="Ví dụ: MEMORY_MANAGEMENT" required />
        </div>
        <button style={styles.button} type="submit" disabled={loading}>
          {loading ? 'AI Đang phân tích...' : 'Gửi Yêu Cầu Phân Tích'}
        </button>
      </form>

      {error && <div style={styles.error}>❌ {error}</div>}

      {prediction && (
        <div style={styles.resultBox}>
          <h3 style={styles.resultTitle}>🤖 Kết luận từ Trí Tuệ Nhân Tạo:</h3>
          <p style={{ margin: 0, fontSize: '18px' }}><strong>{prediction}</strong></p>
        </div>
      )}
    </div>
  );
}

export default App;