const DecisionMakingFacility = () => {
        return (
            <div>
                <Dashboard />
                <DecisionRuleBuilder />
                <ToleranceSettingTools />
                <DecisionLogs />
            </div>
        )
    }

    const Dashboard = () => {
        return (
            <div>
                <DecisionMetrics />
                <SystemRecommendations />
            </div>
        )
    }

    const DecisionRuleBuilder = () => {
        return (
            <div>
                <DecisionRules />
                <RuleManager />
            </div>
        )
    }

    const ToleranceSettingTools = () => {
        return (
            <div>
                <ToleranceSettings />
                <PredictiveAdjustments />
            </div>
        )
    }

    const DecisionLogs = () => {
        return (
            <div>
                <DecisionLogsList />
                <AnalysisReports />
            </div>
        )
    }

    // Export the DecisionMakingFacility component
    export default DecisionMakingFacility;