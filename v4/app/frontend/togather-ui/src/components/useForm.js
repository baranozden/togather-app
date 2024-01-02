import axios from 'axios';
import { useState, useEffect } from 'react';

const useForm = (callback) => {
    const [values, setValues] = useState({
        username: '',
        email: '',
        password: '',
        password2: ''
    });
    const [errors, setErrors] = useState({});
    const [isSubmitting, setIsSubmitting] = useState(false);

    async function submitLogin(user) {
        setErrors({})
        try {
            const {data} = await axios.post(
                'http://localhost:8000/api/login',
                user,
                {headers: {'Content-Type': 'application/json'}},
                {withCredentials: true}
            )

            localStorage.clear();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            localStorage.setItem('username', data.username);
            axios.defaults.headers.common['Authorization'] = 
                                            `Bearer ${data['access']}`;
            
        } catch (e) {
            setErrors({
                password: "Username or Password Invalid"
            }); 
        }
        setIsSubmitting(true);
    };

    const handleChange = e => {
        const { name, value } = e.target;
        setValues({
        ...values,
        [name]: value
        });
    };

    const handleSubmit = e => {
        e.preventDefault();
        // setErrors(validate(values));
        //setIsSubmitting(true);
        submitLogin(values);
    };

    useEffect(
        () => {
            if (Object.keys(errors).length === 0 && isSubmitting) {
                callback();
            }
        },
        [errors] // to run if only errors changed replace with [errors]
    );

    return { handleChange, handleSubmit, values, errors };
};

export default useForm;