'use client'

import { useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

interface FormData {
  Gender: string
  EthnicGroup: string
  ParentEduc: string
  LunchType: string
  TestPrep: string
  ParentMaritalStatus: string
  PracticeSport: string
  IsFirstChild: string
  NrSiblings: number
  TransportMeans: string
  WklyStudyHours: string
  MathScore: number
  WritingScore: number
}


interface PredictionResponse {
  Predicted_ReadingScore: number
}

export default function Home() {
  const [formData, setFormData] = useState<FormData>({
    Gender: '',
    EthnicGroup: '',
    ParentEduc: '',
    LunchType: '',
    TestPrep: '',
    ParentMaritalStatus: '',
    PracticeSport: '',
    IsFirstChild: '',
    NrSiblings: 0,
    TransportMeans: '',
    WklyStudyHours: '',
    MathScore: 0,
    WritingScore: 0
  })



  const [prediction, setPrediction] = useState<number | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleInputChange = (field: keyof FormData, value: string | number) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setPrediction(null)

    try {
      // Map PascalCase keys to snake_case keys to match FastAPI backend
      const payload = {
        gender: formData.Gender,
        ethnic_group: formData.EthnicGroup,
        parent_educ: formData.ParentEduc,
        lunch_type: formData.LunchType,
        test_prep: formData.TestPrep,
        parent_marital_status: formData.ParentMaritalStatus,
        practice_sport: formData.PracticeSport,
        is_first_child: formData.IsFirstChild,
        nr_siblings: formData.NrSiblings,
        transport_means: formData.TransportMeans,
        wkly_study_hours: formData.WklyStudyHours,
        math_score: formData.MathScore,
        writing_score: formData.WritingScore
      }

      console.log("Sending payload:", payload)

      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      })

      if (!response.ok) {
        throw new Error('Failed to get prediction')
      }

      const data = await response.json()
      setPrediction(data.predicted_reading_score)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }


  const isFormValid = () => {
    return Object.values(formData).every(value => 
      value !== '' && value !== 0
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Reading Score Predictor
          </h1>
          <p className="text-lg text-gray-600">
            Predict student reading scores based on various academic and demographic features
          </p>
        </div>

        <Card className="shadow-xl">
          <CardHeader>
            <CardTitle>Student Information Form</CardTitle>
            <CardDescription>
              Please fill in all the required fields to get a reading score prediction
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Gender */}
                <div className="space-y-2">
                  <Label htmlFor="gender">Gender *</Label>
                  <Select value={formData.Gender} onValueChange={(value) => handleInputChange('Gender', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select gender" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="male">Male</SelectItem>
                      <SelectItem value="female">Female</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Ethnic Group */}
                <div className="space-y-2">
                  <Label htmlFor="ethnicGroup">Ethnic Group *</Label>
                  <Select value={formData.EthnicGroup} onValueChange={(value) => handleInputChange('EthnicGroup', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select ethnic group" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="group A">Group A</SelectItem>
                      <SelectItem value="group B">Group B</SelectItem>
                      <SelectItem value="group C">Group C</SelectItem>
                      <SelectItem value="group D">Group D</SelectItem>
                      <SelectItem value="group E">Group E</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Parents' Education */}
                <div className="space-y-2">
                  <Label htmlFor="parentEduc">Parents' Education *</Label>
                  <Select value={formData.ParentEduc} onValueChange={(value) => handleInputChange('ParentEduc', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select education level" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="some_highschool">Some High School</SelectItem>
                      <SelectItem value="high school">High School</SelectItem>
                      <SelectItem value="some college">Some College</SelectItem>
                      <SelectItem value="associate's degree">Associate's Degree</SelectItem>
                      <SelectItem value="bachelor's degree">Bachelor's Degree</SelectItem>
                      <SelectItem value="master's degree">Master's Degree</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Lunch Type */}
                <div className="space-y-2">
                  <Label htmlFor="lunchType">Lunch Type *</Label>
                  <Select value={formData.LunchType} onValueChange={(value) => handleInputChange('LunchType', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select lunch type" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="standard">Standard</SelectItem>
                      <SelectItem value="free/reduced">Free/Reduced</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Test Prep Course */}
                <div className="space-y-2">
                  <Label htmlFor="testPrep">Test Prep Course *</Label>
                  <Select value={formData.TestPrep} onValueChange={(value) => handleInputChange('TestPrep', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select test prep status" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="none">None</SelectItem>
                      <SelectItem value="completed">Completed</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Parents' Marital Status */}
                <div className="space-y-2">
                  <Label htmlFor="parentMaritalStatus">Parents' Marital Status *</Label>
                  <Select value={formData.ParentMaritalStatus} onValueChange={(value) => handleInputChange('ParentMaritalStatus', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select marital status" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="married">Married</SelectItem>
                      <SelectItem value="single">Single</SelectItem>
                      <SelectItem value="widowed">Widowed</SelectItem>
                      <SelectItem value="divorced">Divorced</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Practice Sport */}
                <div className="space-y-2">
                  <Label htmlFor="practiceSport">Practice Sport *</Label>
                  <Select value={formData.PracticeSport} onValueChange={(value) => handleInputChange('PracticeSport', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select sport practice frequency" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="never">Never</SelectItem>
                      <SelectItem value="sometimes">Sometimes</SelectItem>
                      <SelectItem value="regularly">Regularly</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Is First Child */}
                <div className="space-y-2">
                  <Label htmlFor="isFirstChild">Is First Child? *</Label>
                  <Select value={formData.IsFirstChild} onValueChange={(value) => handleInputChange('IsFirstChild', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select first child status" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="yes">Yes</SelectItem>
                      <SelectItem value="no">No</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Number of Siblings */}
                <div className="space-y-2">
                  <Label htmlFor="nrSiblings">Number of Siblings *</Label>
                  <Input
                    id="nrSiblings"
                    type="number"
                    min="0"
                    max="7"
                    value={formData.NrSiblings}
                    onChange={(e) => handleInputChange('NrSiblings', parseInt(e.target.value) || 0)}
                    placeholder="0-7"
                  />
                </div>

                {/* Transport Means */}
                <div className="space-y-2">
                  <Label htmlFor="transportMeans">Transport Means *</Label>
                  <Select value={formData.TransportMeans} onValueChange={(value) => handleInputChange('TransportMeans', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select transport method" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="schoolbus">School Bus</SelectItem>
                      <SelectItem value="private">Private</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Weekly Study Hours */}
                <div className="space-y-2">
                  <Label htmlFor="wklyStudyHours">Weekly Study Hours *</Label>
                  <Select value={formData.WklyStudyHours} onValueChange={(value) => handleInputChange('WklyStudyHours', value)}>
                    <SelectTrigger>
                      <SelectValue placeholder="Select study hours" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="less than 5hrs">Less than 5 hours</SelectItem>
                      <SelectItem value="between 5 and 10hrs">Between 5 and 10 hours</SelectItem>
                      <SelectItem value="more than 10hrs">More than 10 hours</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                {/* Math Score */}
                <div className="space-y-2">
                  <Label htmlFor="mathScore">Math Score *</Label>
                  <Input
                    id="mathScore"
                    type="number"
                    min="0"
                    max="100"
                    value={formData.MathScore}
                    onChange={(e) => handleInputChange('MathScore', parseInt(e.target.value) || 0)}
                    placeholder="0-100"
                  />
                </div>

                {/* Writing Score */}
                <div className="space-y-2">
                  <Label htmlFor="writingScore">Writing Score *</Label>
                  <Input
                    id="writingScore"
                    type="number"
                    min="0"
                    max="100"
                    value={formData.WritingScore}
                    onChange={(e) => handleInputChange('WritingScore', parseInt(e.target.value) || 0)}
                    placeholder="0-100"
                  />
                </div>
              </div>

              <div className="flex justify-center pt-4">
                <Button
                  type="submit"
                  disabled={!isFormValid() || loading}
                  className="px-8 py-3 text-lg"
                >
                  {loading ? 'Predicting...' : 'Predict Reading Score'}
                </Button>
              </div>
            </form>

            {/* Prediction Result */}
            {prediction !== null && (
              <div className="mt-8 p-6 bg-green-50 border border-green-200 rounded-lg">
                <h3 className="text-xl font-semibold text-green-800 mb-2">
                  Prediction Result
                </h3>
                <p className="text-3xl font-bold text-green-600">
                  {prediction.toFixed(1)}
                </p>
                <p className="text-green-700 mt-1">Predicted Reading Score</p>
              </div>
            )}

            {/* Error Message */}
            {error && (
              <div className="mt-8 p-6 bg-red-50 border border-red-200 rounded-lg">
                <h3 className="text-xl font-semibold text-red-800 mb-2">
                  Error
                </h3>
                <p className="text-red-700">{error}</p>
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
