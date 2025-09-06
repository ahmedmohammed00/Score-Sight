# Reading Score Predictor

A Next.js web application for predicting student reading scores based on various academic and demographic features. Built with Next.js 14, TypeScript, Tailwind CSS, and shadcn/ui components.

## Features

- **Comprehensive Form**: Collects 13 different student features including:
  - Demographics (Gender, Ethnic Group)
  - Family background (Parents' Education, Marital Status, Number of Siblings)
  - Academic factors (Test Prep, Study Hours, Math Score, Writing Score)
  - Lifestyle factors (Lunch Type, Sport Practice, Transport)

- **Modern UI**: Beautiful, responsive interface built with shadcn/ui components
- **Form Validation**: Ensures all required fields are completed before submission
- **Real-time Feedback**: Shows loading states and error messages
- **Prediction Display**: Clearly presents the predicted reading score

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui (Radix UI primitives)
- **State Management**: React hooks
- **API**: Next.js API routes

## Prerequisites

- Node.js 18+ 
- npm or yarn

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd reading-score-predictor
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:3000
   ```

## Project Structure

```
reading-score-predictor/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── predict/
│   │   │       └── route.ts          # API endpoint for predictions
│   │   ├── globals.css               # Global styles and Tailwind imports
│   │   ├── layout.tsx                # Root layout component
│   │   └── page.tsx                  # Main page with the form
│   ├── components/
│   │   └── ui/                       # shadcn/ui components
│   │       ├── button.tsx
│   │       ├── card.tsx
│   │       ├── input.tsx
│   │       ├── label.tsx
│   │       └── select.tsx
│   └── lib/
│       └── utils.ts                  # Utility functions
├── package.json
├── tailwind.config.js                # Tailwind CSS configuration
├── tsconfig.json                     # TypeScript configuration
└── README.md
```

## Form Fields

The application collects the following student features:

1. **Gender**: Male/Female
2. **Ethnic Group**: Group A, B, C, D, or E
3. **Parents' Education**: From some high school to master's degree
4. **Lunch Type**: Standard or free/reduced
5. **Test Prep Course**: None or completed
6. **Parents' Marital Status**: Married, single, widowed, or divorced
7. **Practice Sport**: Never, sometimes, or regularly
8. **Is First Child**: Yes or no
9. **Number of Siblings**: 0-7
10. **Transport Means**: School bus or private
11. **Weekly Study Hours**: Less than 5hrs, 5-10hrs, or more than 10hrs
12. **Math Score**: 0-100
13. **Writing Score**: 0-100

## API Endpoint

The application includes a mock API endpoint at `/api/predict` that:

- Accepts POST requests with the student data
- Validates all required fields
- Returns a predicted reading score
- Currently uses a mock algorithm (replace with your ML model)

### Request Format
```json
{
  "Gender": "female",
  "EthnicGroup": "group B",
  "ParentEduc": "bachelor's degree",
  "LunchType": "standard",
  "TestPrep": "none",
  "ParentMaritalStatus": "single",
  "PracticeSport": "sometimes",
  "IsFirstChild": "yes",
  "NrSiblings": 2,
  "TransportMeans": "schoolbus",
  "WklyStudyHours": "between 5 and 10hrs",
  "MathScore": 78,
  "WritingScore": 82
}
```

### Response Format
```json
{
  "Predicted_ReadingScore": 86.5
}
```

## Customization

### Replacing the Mock Prediction

To integrate with a real ML model:

1. **Update the API route** in `src/app/api/predict/route.ts`
2. **Replace the mock algorithm** with calls to your ML model API
3. **Handle authentication** if required by your ML service
4. **Add error handling** for ML model failures

### Styling

- **Colors**: Modify CSS variables in `src/app/globals.css`
- **Layout**: Adjust Tailwind classes in the components
- **Theme**: Update `tailwind.config.js` for custom design tokens

### Form Validation

- **Client-side**: Modify validation logic in `src/app/page.tsx`
- **Server-side**: Update validation in the API route

## Building for Production

1. **Build the application:**
   ```bash
   npm run build
   ```

2. **Start the production server:**
   ```bash
   npm start
   ```

## Deployment

This Next.js application can be deployed to:

- **Vercel** (recommended for Next.js)
- **Netlify**
- **AWS Amplify**
- **Any Node.js hosting platform**

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue in the repository or contact the development team.
