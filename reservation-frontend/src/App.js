import React, { useState } from 'react';

function App() {
  const [form, setForm] = useState({
    reservation_id: '',
    property_name: '',
    host_name: '',
    guest_name: '',
    check_in_date: '',
    price_per_night: '',
  });

  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const res = await fetch("http://localhost:8082/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await res.json();
      alert("Response:\n" + JSON.stringify(data, null, 2));
    } catch (error) {
      alert("Error:\n" + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  const getFieldIcon = (fieldName) => {
    const icons = {
      reservation_id: '🏷️',
      property_name: '🏠',
      host_name: '👤',
      guest_name: '👥',
      check_in_date: '📅',
      price_per_night: '💰'
    };
    return icons[fieldName] || '📝';
  };

  const getFieldType = (fieldName) => {
    if (fieldName === 'check_in_date') return 'date';
    if (fieldName === 'price_per_night') return 'number';
    return 'text';
  };

  const formatLabel = (key) => {
    return key.replace(/_/g, ' ')
      .split(' ')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-purple-600 px-8 py-6">
            <h2 className="text-3xl font-bold text-white text-center">
              Креирај Резервација
            </h2>
            <p className="text-blue-100 text-center mt-2">
              Пополни ги сите потребни информации
            </p>
          </div>

          {/* Form */}
          <div className="p-8 space-y-6">
            {Object.keys(form).map((key) => (
              <div key={key} className="group">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {formatLabel(key)}
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-gray-400 group-focus-within:text-blue-500 transition-colors text-xl">
                    {getFieldIcon(key)}
                  </div>
                  <input
                    name={key}
                    type={getFieldType(key)}
                    value={form[key]}
                    onChange={handleChange}
                    placeholder={`Внеси ${formatLabel(key).toLowerCase()}`}
                    className="w-full pl-16 pr-4 py-4 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-gray-50 focus:bg-white hover:bg-white"
                    required
                  />
                </div>
              </div>
            ))}

            <button
              type="button"
              onClick={handleSubmit}
              disabled={isLoading}
              className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-bold py-4 px-8 rounded-xl transition-all duration-200 transform hover:scale-[1.02] focus:scale-[0.98] shadow-lg hover:shadow-xl"
            >
              {isLoading ? (
                <div className="flex items-center justify-center">
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                  Се обработува...
                </div>
              ) : (
                'Креирај Резервација'
              )}
            </button>
          </div>

          {/* Footer */}
          <div className="bg-gray-50 px-8 py-4 border-t border-gray-100">
            <p className="text-sm text-gray-500 text-center">
              Сите полиња се задолжителни за пополнување
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;