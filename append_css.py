import os

css_append = '''

/* ==========================================================================
   REFERRAL FORM MODULE STYLES
   ========================================================================== */
.referral-layout {
    display: flex;
    gap: 40px;
    align-items: flex-start;
}

.referral-form-wrapper {
    flex: 2;
}

.referral-sidebar-wrapper {
    flex: 1;
    position: sticky;
    top: 100px;
}

@media (max-width: 992px) {
    .referral-layout {
        flex-direction: column;
    }
    .referral-sidebar-wrapper {
        position: static;
        width: 100%;
    }
}

.form-section-title {
    color: var(--primary);
    font-size: 1.5rem;
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 10px;
    margin-bottom: 20px;
    font-family: var(--font-heading);
}

.checkbox-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 15px;
}

.custom-checkbox {
    display: flex;
    align-items: center;
    gap: 10px;
}

.custom-checkbox input[type="checkbox"] {
    width: 20px;
    height: 20px;
    accent-color: var(--secondary);
    cursor: pointer;
}

.custom-checkbox label {
    margin-bottom: 0;
    cursor: pointer;
    font-size: 0.95rem;
    color: var(--heading);
}

.process-list {
    list-style: none;
    padding: 0;
}

.process-list li {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
}

.process-list .step-num {
    background: var(--primary);
    color: var(--white);
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    flex-shrink: 0;
}

.process-list p {
    margin: 0;
    font-size: 0.95rem;
    font-weight: 500;
}

.check-list {
    list-style: none;
    padding: 0;
}

.check-list li {
    margin-bottom: 12px;
    font-size: 0.95rem;
}
'''

with open('d:/projects/caraamax/static/css/styles.css', 'a') as f:
    f.write(css_append)
print("CSS appended.")
